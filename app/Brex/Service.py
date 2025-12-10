from app.Brex.Client  import BrexClient
from urllib.parse import unquote
from fastapi import HTTPException
from datetime import timezone, datetime

client = BrexClient()


def costos_CAC( start_date: str, end_date: str | None = None, acumulado:bool | None = None):

    if end_date is None:
        # generar fecha actual en formato RFC3339
        end_date = datetime.now(timezone.utc).isoformat()
    # Decodificar %3A
    start_date = unquote(start_date)
    end_date = unquote(end_date)

    # Asegurar formato RFC 3339 con milisegundos
    if len(start_date) == 19:
        start_date += ".000"
    if len(end_date) == 19:
        end_date += ".000"

    expenses = client.get_expenses_paginated({
        "purchased_at_start": start_date,
        "purchased_at_end": end_date},"/expenses/card")

    print("DEBUG PAGOS:", expenses)

    # Validar respuesta de Brex
    if not isinstance(expenses, list):
        raise HTTPException(
            status_code=500,
            detail=f"Brex error response: {expenses}"
        )
    
    SOFTWARE_MERCHANT_IDS = {
    "pmch_cg0l843lp00401kd8v4gmkyt": "facebook",
    "pmch_cka6y763600bh01kl76k2ks1j": "Tiktok",
    "pmch_cl6dvvlpr02qr0mnaf13xinsz": "Linkedin",
    "pmch_cc8awwmzp18pi1cbcw6qe8ms": "Google adds"
}    
    resumen = {}

    # -------- CASE 1: DETALLADO --------
    if acumulado is False:
        for gasto in expenses:
            vendor = gasto.get("merchant_id")
            if vendor not in SOFTWARE_MERCHANT_IDS:
                continue

            vendor_name = SOFTWARE_MERCHANT_IDS[vendor]
            amount = gasto["original_amount"]["amount"] / 100
            fecha = gasto["purchased_at"][:7]

            if fecha not in resumen:
                resumen[fecha] = {}

            resumen[fecha][vendor_name] = resumen[fecha].get(vendor_name, 0) + amount

        return resumen

    # -------- CASE 2: ACUMULADO TOTAL --------
    if acumulado is True:
        for gasto in expenses:
            vendor = gasto.get("merchant_id")
            if vendor not in SOFTWARE_MERCHANT_IDS:
                continue

            amount = gasto["original_amount"]["amount"] / 100
            fecha = gasto["purchased_at"][:7]

            if fecha not in resumen:
                resumen[fecha] = 0

            resumen[fecha] += amount

        return resumen

    # -------- CASE 3: DEFAULT (ACUMULADO) --------
    for gasto in expenses:
        vendor = gasto.get("merchant_id")
        if vendor not in SOFTWARE_MERCHANT_IDS:
            continue

        amount = gasto["original_amount"]["amount"] / 100
        fecha = gasto["purchased_at"][:7]

        if fecha not in resumen:
            resumen[fecha] = 0

        resumen[fecha] += amount

    return resumen



def costos_UE( start_date: str, end_date:str, acumulado: bool | None=None):

    # Decodificar %3A
    start_date = unquote(start_date)
    end_date = unquote(end_date)

    # Asegurar formato RFC 3339 con milisegundos
    if len(start_date) == 19:
        start_date += ".000"
    if len(end_date) == 19:
        end_date += ".000"

    expenses = client.get_expenses_paginated({
        "purchased_at_start": start_date,
        "purchased_at_end": end_date,
        },"/expenses/card")

    print("DEBUG PAGOS:", expenses)

    # Validar respuesta de Brex
    if not isinstance(expenses, list):
        raise HTTPException(
            status_code=500,
            detail=f"Brex error response: {expenses}"
        )
    resumen = {}


    SOFTWARE_MERCHANT_IDS = {
    "pmch_cmctm4ot50dq70i40pzlg3d7p": "Enrich",
    "pmch_cjyz16z7v03rg0141l7tmp2ft": "Apollo",
    "pmch_ckom0mtgm0dt601k9c134eftb": "Supabase",
    "pmch_cq5icnwpt00ne6hd09ih1l6f": "Google Cloud"
}
    
    if acumulado is True:

        for gasto in expenses: 
             vendor = gasto.get("merchant_id") or "unknown"
             if vendor not in SOFTWARE_MERCHANT_IDS:
              continue
             vendo = SOFTWARE_MERCHANT_IDS[vendor]
             amount_cents = gasto["original_amount"]["amount"]
             amount = amount_cents / 100 
             fecha = gasto["purchased_at"][:7]

             if fecha not in resumen:
              resumen[fecha] = 0

             resumen[fecha] += amount
        return resumen
    
    if acumulado is False:

        for gasto in expenses: 
             vendor = gasto.get("merchant_id") or "unknown"
             if vendor not in SOFTWARE_MERCHANT_IDS:
               continue
             vendo = SOFTWARE_MERCHANT_IDS[vendor]
             amount_cents = gasto["original_amount"]["amount"]
             amount = amount_cents / 100 
             fecha = gasto["purchased_at"][:7]

             if fecha not in resumen:
              resumen[fecha] = {}

             resumen[fecha][vendo] = resumen[fecha].get(vendo, 0) + amount
        return resumen

    for gasto in expenses: 
             vendor = gasto.get("merchant_id") or "unknown"
             if vendor not in SOFTWARE_MERCHANT_IDS:
              continue
             vendo = SOFTWARE_MERCHANT_IDS[vendor]
             amount_cents = gasto["original_amount"]["amount"]
             amount = amount_cents / 100 
             fecha = gasto["purchased_at"][:7]

             if fecha not in resumen:
              resumen[fecha] = 0

             resumen[fecha] += amount
    return resumen








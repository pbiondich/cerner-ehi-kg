# RXS_RECEIVING_DETAIL

> Stores details captured by the user during the Controlled Substance Vault (CSV) Receiving workflow.

**Description:** RxStation Receiving Detail  
**Table type:** ACTIVITY  
**Primary key:** `RXS_RECEIVING_DETAIL_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSOS_IDENT` | VARCHAR(255) |  |  | CSOS Identifier |
| 2 | `DEA_CS_FORM_222_IDENT` | VARCHAR(255) | NOT NULL |  | The identifier for the control substance received. |
| 3 | `INVOICE_NBR_TXT` | VARCHAR(255) | NOT NULL |  | Textual representation of the invoice number for the drug being received. |
| 4 | `MISC_IDENT_TXT` | VARCHAR(255) |  |  | Allows non-defined identifiers to be added. |
| 5 | `PO_NBR_TXT` | VARCHAR(255) | NOT NULL |  | Textual representation of the purchase order number for the drug being received. |
| 6 | `RXS_RECEIVING_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_RECEIVING_DETAIL table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VENDOR_NAME_TXT` | VARCHAR(255) |  |  | A short description of the vendor name. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_RECEIVING_DETAIL_ID` |


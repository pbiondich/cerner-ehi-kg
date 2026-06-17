# MLTM_RXB_ORDER_REFILL_MAP

> Multum Rx Builder Order Refill Map Table

**Description:** Multum Rx Builder Order Refill Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL | FK→ | Drug Identifier |
| 2 | `ORDER_ID_NBR` | DOUBLE | NOT NULL | FK→ | This field contains an identifier that provides uniqueness to a record and along with the drug_id associates a record with a main_Multum_drug_code. |
| 3 | `REFILL_AMOUNT` | DOUBLE | NOT NULL |  | Refill Amount Value |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER` | [MLTM_RXB_ORDER](MLTM_RXB_ORDER.md) | `DRUG_IDENTIFIER` |
| `ORDER_ID_NBR` | [MLTM_RXB_ORDER](MLTM_RXB_ORDER.md) | `ORDER_ID_NBR` |


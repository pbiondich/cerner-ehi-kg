# RX_PENDING_CHARGE

> The Pharmacy Pending Charge identifies Medication Administration Record (MAR) events and ingredients that have charges waiting for Pharmacist Verification. Once verified, the Pending charge is either deleted, posted or appears in PhaChargeCredit.

**Description:** Pharmacy Pending Charge table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | Identifies core action sequence of Pharmacy Pending Charge. |
| 2 | `ADMIN_DT_TM` | DATETIME | NOT NULL |  | Identifies administration date/time of Medication Administration event. |
| 3 | `ADMIN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `COMP_SEQUENCE` | DOUBLE | NOT NULL |  | Identifies component sequence of Pharmacy Pending Charge. |
| 5 | `DOSE` | DOUBLE | NOT NULL |  | Identifies ingredient dose of Medication Administration event. |
| 6 | `DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies ingredient dose unit of Medication Administration event. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifies Clinical Event related to Pharmacy Pending Charge. |
| 8 | `INGRED_ACTION_SEQ` | DOUBLE | NOT NULL |  | Identifies ingredient action sequence of Pharmacy Pending Charge. |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies Orders related to Pharmacy Pending Charge. |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies administration personnel of Medication Administration event. |
| 11 | `ROUTE_CD` | DOUBLE | NOT NULL |  | Identifies route of Medication Administration event |
| 12 | `RX_PENDING_CHARGE_ID` | DOUBLE | NOT NULL |  | Unique field for Rx_pending_charge table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Identifies when the Clinical Event is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


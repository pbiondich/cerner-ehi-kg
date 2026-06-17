# RX_PENDING_CHARGE_DELETED

> Replica of rx_pending_charge table. It will hold the values deleted from rx_pending_charge.

**Description:** Pharmacy Pending Charge Deleted  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE |  | FK→ | Identifies core action sequence of Pharmacy Pending Charge. |
| 2 | `ADMIN_DT_TM` | DATETIME |  |  | Identifies administration date/time of Medication Administration event. |
| 3 | `ADMIN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `COMP_SEQUENCE` | DOUBLE |  |  | Identifies component sequence of Pharmacy Pending Charge. |
| 5 | `DOSE` | DOUBLE |  |  | Identifies ingredient dose of Medication Administration event. |
| 6 | `DOSE_UNIT_CD` | DOUBLE |  |  | Identifies ingredient dose unit of Medication Administration event. |
| 7 | `EVENT_ID` | DOUBLE |  |  | Identifies Clinical Event related to Pharmacy Pending Charge. |
| 8 | `INGRED_ACTION_SEQ` | DOUBLE |  |  | Identifies ingredient action sequence of Pharmacy Pending Charge. |
| 9 | `ORDER_ID` | DOUBLE |  | FK→ | Identifies Orders related to Pharmacy Pending Charge. |
| 10 | `PRSNL_ID` | DOUBLE |  | FK→ | Identifies administration personnel of Medication Administration event. |
| 11 | `ROUTE_CD` | DOUBLE |  |  | Identifies route of Medication Administration event |
| 12 | `RX_PENDING_CHARGE_DELETED_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_PENDING_CHARGE_DELETED table. |
| 13 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | Identifies when the Clinical Event is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


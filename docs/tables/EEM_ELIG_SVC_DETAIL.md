# EEM_ELIG_SVC_DETAIL

> EEM Eligibility Service Details table

**Description:** EEM Eligibility Service Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EEM_ELIG_SVC_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary identifier for EEM_ELIG_SVC_DETAIL |
| 2 | `EEM_RX_ELIG_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Primary identifier for EEM_RX_ELIG_DETAIL |
| 3 | `ELIGIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | Denotes if a service is eligible or not eligible |
| 4 | `INTERCHANGE_ID` | DOUBLE | NOT NULL | FK→ | Primary identifier for a transaction |
| 5 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of service for eligibility or benefit details |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EEM_RX_ELIG_DETAIL_ID` | [EEM_RX_ELIG_DETAIL](EEM_RX_ELIG_DETAIL.md) | `EEM_RX_ELIG_DETAIL_ID` |
| `INTERCHANGE_ID` | [EEM_TRANSACTION](EEM_TRANSACTION.md) | `TRANSACTION_ID` |


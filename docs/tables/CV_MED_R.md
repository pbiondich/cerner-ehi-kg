# CV_MED_R

> Relates CV_PROC to ORDER (Pharmacy - Medication Orders)

**Description:** CV Medication Order relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CV_MED_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `CV_PROC_ID` | DOUBLE | NOT NULL | FK→ | Procedure_ID of the Cardiovascular procedure from CV_PROC table for which a medication order has been placed |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event_ID for the action performed on the Pharmacy order from CLINICAL_EVENT table. |
| 4 | `MED_REF_LOG_EVENT_VALUE` | DOUBLE | NOT NULL |  | Medication Reference Event Value |
| 5 | `PHARM_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_ID of the pharmacy order from ORDERS table |
| 6 | `STATUS_TXT` | VARCHAR(30) | NOT NULL |  | The state indicates the point at which a failure occurred or a successful completion. The possible states: 0 - NOT STARTED 1 - IN PROCESS 2 - ORDER 3 - CLINICAL EVENT 4 - CHARGE 5 - COMPLETED |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_PROC_ID` | [CV_PROC](CV_PROC.md) | `CV_PROC_ID` |
| `PHARM_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |


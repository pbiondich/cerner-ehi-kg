# ONC_INFUSION_ACTIVITY

> Stores the oncology infusion activity

**Description:** ONCOLOGY INFUSION ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIN_ROUTE_TYPE_TXT` | VARCHAR(100) | NOT NULL |  | A short display string to indicate the type of the route selected for the event |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | encounter for which this event is charted |
| 4 | `EVENT_STATUS_TXT` | VARCHAR(20) | NOT NULL |  | A short display string to indicate the status of the event documented. |
| 5 | `ONC_INFUSION_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | order id for which event is charted. |
| 7 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | highest level event id from the CLINICAL_EVENT table for the documented order. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom this event is charted. |
| 9 | `SERVICE_DT_TM` | DATETIME |  |  | Date and time of the event charted. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |


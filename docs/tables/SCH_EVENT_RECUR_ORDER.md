# SCH_EVENT_RECUR_ORDER

> Table used to record the orderables which will be attached to the recurring instances.

**Description:** Scheduling Event Recurring Order  
**Table type:** ACTIVITY  
**Primary key:** `SCH_EVENT_RECUR_ORDER_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism within catalog type code |
| 2 | `EVENT_RECUR_ID` | DOUBLE | NOT NULL | FK→ | the identifier from sch_event_recur table |
| 3 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Order physician's personnal Id |
| 4 | `ORDER_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Id of the synonym for this order |
| 5 | `SCH_EVENT_RECUR_ORDER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_ORDER table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_RECUR_ID` | [SCH_EVENT_RECUR](SCH_EVENT_RECUR.md) | `EVENT_RECUR_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_EVENT_RECUR_ORD_DETAIL](SCH_EVENT_RECUR_ORD_DETAIL.md) | `SCH_EVENT_RECUR_ORDER_ID` |


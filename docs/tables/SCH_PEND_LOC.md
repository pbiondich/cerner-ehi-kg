# SCH_PEND_LOC

> Contains location information about an appointment which will be created.

**Description:** Scheduling Pending Location  
**Table type:** ACTIVITY  
**Primary key:** `SCH_PEND_LOC_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location to be considered for this pending event. |
| 2 | `SCH_PEND_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The pending event identifier that this data belongs to. |
| 3 | `SCH_PEND_LOC_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_PEND_LOC table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `SCH_PEND_EVENT_ID` | [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `SCH_PEND_EVENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_PEND_RES](SCH_PEND_RES.md) | `SCH_PEND_LOC_ID` |


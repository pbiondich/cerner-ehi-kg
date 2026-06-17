# HIM_RESTRICT_VIEW_HIST

> HIM restrict view history

**Description:** HIM RESTRICT VIEW HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HIM_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The primary key of him_request table |
| 2 | `HIM_REQUEST_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | him request patient identifier |
| 3 | `HIM_RESTRICT_VIEW_HIST_ID` | DOUBLE | NOT NULL |  | him restrict view history identifier |
| 4 | `OVERRIDE_COMMENT` | VARCHAR(255) |  |  | override comment |
| 5 | `OVERRIDE_DT_TM` | DATETIME |  |  | override date and time |
| 6 | `OVERRIDE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | override personnel identifier |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VIEW_DT_TM` | DATETIME | NOT NULL |  | view date and time |
| 13 | `VIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | view personnel identifier |
| 14 | `VIEW_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the restriction Values: 1 - Not Applicable, 2 - Overridden, 3 - Rejected |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIM_REQUEST_ID` | [HIM_REQUEST](HIM_REQUEST.md) | `HIM_REQUEST_ID` |
| `HIM_REQUEST_PATIENT_ID` | [HIM_REQUEST_PATIENT](HIM_REQUEST_PATIENT.md) | `HIM_REQUEST_PATIENT_ID` |
| `OVERRIDE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `VIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


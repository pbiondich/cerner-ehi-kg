# WF_SHIFT_SCHED

> This table stores the shifts created in workforce solution.

**Description:** Work Force Shift Schedule  
**Table type:** ACTIVITY  
**Primary key:** `WF_SHIFT_SCHED_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALL_SHIFT_IND` | DOUBLE |  |  | Used to determine if the shift is a call shift or a standard shift. Typically patients are not assigned to a call shift. |
| 2 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `END_DT_TM` | DATETIME |  |  | The end date/time of the shift. |
| 7 | `END_TZ` | DOUBLE |  |  | The time zone of the shift end. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization to which the shift is assigned. |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the person assigned to the shift. |
| 10 | `PRSNL_LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the person assigned to the shift. |
| 11 | `PRSNL_SHIFT_ROLE_CD` | DOUBLE | NOT NULL |  | The role of the person working the shift. |
| 12 | `SALARIED_PRSNL_IND` | DOUBLE |  |  | Used to determine if the personnel is a salaried employee. |
| 13 | `SHIFT_DESC` | VARCHAR(200) |  |  | Free text description of the shift. |
| 14 | `SHIFT_IDENT` | VARCHAR(100) |  |  | Stores the unique key to the shift in a foreign staff schduling system. |
| 15 | `SHIFT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the shift. |
| 16 | `SHIFT_ROLE_CD` | DOUBLE | NOT NULL |  | The role of the shift. |
| 17 | `START_DT_TM` | DATETIME |  |  | The start date and time of the shift. |
| 18 | `START_TZ` | DOUBLE |  |  | The time zone used to determine the start of the shift. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `WF_SHIFT_SCHED_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a workforce shift schedule. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WF_SHIFT_RESP](WF_SHIFT_RESP.md) | `WF_SHIFT_SCHED_ID` |
| [WF_XFI_SHIFT_SCHED](WF_XFI_SHIFT_SCHED.md) | `WF_SHIFT_SCHED_ID` |


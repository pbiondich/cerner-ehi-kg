# WF_XFI_SHIFT_SCHED

> This is a staging table storing the shift information coming from third party system.

**Description:** Workforce Interface Shift Schedule  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Used to determine the type of action to apply to the record. |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias Pool Code. Used to resolve the personnel. |
| 3 | `ALIAS_POOL_TXT` | VARCHAR(60) |  |  | Alias pool used to resolve the personnel. |
| 4 | `CALL_SHIFT_IND` | DOUBLE |  |  | Used to determine if the shift is a call shift or a standard shift. Typically patients are not assinged to a call shift. |
| 5 | `CONTRIBUTOR` | VARCHAR(60) |  |  | Contains the contributor source of the foreign system used to resolve code values. |
| 6 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor source code. |
| 7 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 11 | `END_DT_TM` | DATETIME |  |  | The end date/time of the shift. |
| 12 | `END_TZ` | DOUBLE |  |  | The time zone of the shift end. |
| 13 | `ORGANIZATION` | VARCHAR(100) |  |  | Contains the organization of the shift location. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization identifier. Used to uniquely identify the organization for this shift schedule. |
| 15 | `PERSON_ALIAS` | VARCHAR(200) |  |  | Person Alias. Alias that will be used to resolve to a millennium personnel. |
| 16 | `PROCESS_FLAG` | DOUBLE |  |  | Flag used to determine the status of the record being processed. |
| 17 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the personnel that is assigned to the shift. |
| 18 | `PRSNL_LOCATION_CD` | DOUBLE | NOT NULL |  | The home location of the personnel. This could be different than the shift location. |
| 19 | `PRSNL_LOCATION_TXT` | VARCHAR(60) |  |  | The home location of the personnel. This could be different than the shift location. |
| 20 | `PRSNL_SHIFT_ROLE_CD` | DOUBLE | NOT NULL |  | The role of the person for the shift. |
| 21 | `PRSNL_SHIFT_ROLE_TXT` | VARCHAR(60) |  |  | The role of the person for the shift. |
| 22 | `SALARIED_PRSNL_IND` | DOUBLE |  |  | Used to determine if the shift is a call shift or a standard shift. Typically patients are not assigned to a call shift. |
| 23 | `SHIFT_DESC` | VARCHAR(200) |  |  | Free text description of the shift. |
| 24 | `SHIFT_IDENT` | VARCHAR(100) |  |  | Used to store the unique value to the shift in a foreign system. |
| 25 | `SHIFT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the shift. |
| 26 | `SHIFT_LOCATION_TXT` | VARCHAR(60) |  |  | The locatin of the shift. |
| 27 | `SHIFT_ROLE_CD` | DOUBLE | NOT NULL |  | The role of the shift. |
| 28 | `SHIFT_ROLE_TXT` | VARCHAR(60) |  |  | The role of the shift. |
| 29 | `START_DT_TM` | DATETIME |  |  | The start date and time of the shift. |
| 30 | `START_TZ` | DOUBLE |  |  | The time zone used to determine the start of the shift. |
| 31 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the wf_xfi_shift_schedule table. Primary Key. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `WF_SHIFT_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the WF_SHIFT_SCHED table related to each row on the WF_XFI_SHIFT_SCHED table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WF_SHIFT_SCHED_ID` | [WF_SHIFT_SCHED](WF_SHIFT_SCHED.md) | `WF_SHIFT_SCHED_ID` |


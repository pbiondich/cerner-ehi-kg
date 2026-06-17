# AP_DC_EVENT_PRSNL

> This activity table includes information about the individual user (or users) or user group members associated with a specific diagnostic correlation event.

**Description:** Diagnostic Correlation Event Personnel  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the diagnostic correlation event. Information about the event can be obtained by viewing or joining to the AP_DC_EVENT table. |
| 2 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | If the diagnostic correlation event was associated with a user group (rather than an individual or set of individuals), this field contains the reference back to the PRSNL_GROUP_ID value for the specific diagnostic correlation study event (as stored on the AP_DC_EVENT table). |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the individual user, users, or group members assigned to the evaluation of the diagnostic correlation event. Information about the user can be obtained by viewing or joining to the PERSON and/or PRSNL tables. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_ID` | [AP_DC_EVENT](AP_DC_EVENT.md) | `EVENT_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


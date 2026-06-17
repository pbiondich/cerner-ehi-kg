# RCA_MOBILE_SESSION

> Stores mobile Kiosk session information for Kiosk Tracking Board in CPM solution.

**Description:** RCA Mobile Session  
**Table type:** ACTIVITY  
**Primary key:** `RCA_MOBILE_SESSION_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter identifier of the mobile session. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person identifier of the mobile session. |
| 3 | `RCA_MOBILE_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the mobile profile. |
| 4 | `RCA_MOBILE_SESSION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RCA_MOBILE_SESSION table. |
| 5 | `SESSION_BEG_DT_TM` | DATETIME | NOT NULL |  | The date and time the mobile session begins. |
| 6 | `SESSION_END_DT_TM` | DATETIME |  |  | The date and time the mobile session ends. |
| 7 | `SESSION_STATE_CD` | DOUBLE | NOT NULL |  | The current state of the mobile session. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RCA_MOBILE_PROFILE_ID` | [RCA_MOBILE_PROFILE](RCA_MOBILE_PROFILE.md) | `RCA_MOBILE_PROFILE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCA_MOBILE_SESSION_ACT](RCA_MOBILE_SESSION_ACT.md) | `RCA_MOBILE_SESSION_ID` |


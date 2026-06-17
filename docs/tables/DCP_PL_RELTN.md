# DCP_PL_RELTN

> Makes patient lists available to other related users with defined proxy access (MAINTAIN, OWNER,READ)..

**Description:** DCP PL RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `DCP_MP_PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the list from the DCP_MP_PATIENT_LIST table that is being shared. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LIST_ACCESS_CD` | DOUBLE | NOT NULL |  | Defines what level of access the user(s) will have for this patient list. |
| 5 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the patient list to be related. |
| 6 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The prsnl group id that is to be granted access to the patient list. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the user to be granted access to the list. |
| 8 | `RELTN_ID` | DOUBLE | NOT NULL |  | The unique identifier of the patient list relationship. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_MP_PATIENT_LIST_ID` | [DCP_MP_PATIENT_LIST](DCP_MP_PATIENT_LIST.md) | `DCP_MP_PATIENT_LIST_ID` |
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


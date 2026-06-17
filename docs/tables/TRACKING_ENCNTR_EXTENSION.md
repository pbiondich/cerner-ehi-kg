# TRACKING_ENCNTR_EXTENSION

> Store tracking specific data elements related to an encounter. Used in cases where no tracking id is available (CWD for example).

**Description:** Tracking Encounter Extension  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DC_SIGNED_IND` | DOUBLE | NOT NULL |  | Indicates that the discharge process has been signed |
| 2 | `DC_SIGNED_USER_ID` | DOUBLE | NOT NULL | FK→ | Provider who last signed the discharge process. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encntr_id of the associated encounter record. |
| 4 | `ESIGNATURE_FLAG` | DOUBLE | NOT NULL |  | status of the eSignature for an encounter. 0 = not complete, 1 = all fields complete, 2 = at least 1 signature was declined. |
| 5 | `PAT_ED_ACKNOWLEDGED_IND` | DOUBLE | NOT NULL |  | Indicates the patient understands the instructions they were given. |
| 6 | `PAT_ED_ACKNOWLEDGED_USER_ID` | DOUBLE | NOT NULL | FK→ | The id of the provider who last set the patient acknowledgement indicator true |
| 7 | `PAT_RECEIVED_EC_IND` | DOUBLE | NOT NULL |  | Patient received an electronic copy of the discharge patient summary |
| 8 | `PAT_RECEIVED_EC_USER_ID` | DOUBLE | NOT NULL |  | User id of prsnl performing action |
| 9 | `PAT_REQUESTED_EC_IND` | DOUBLE | NOT NULL |  | Patient requested an electronic copy of the discharge patient summary |
| 10 | `PAT_REQUESTED_EC_USER_ID` | DOUBLE | NOT NULL |  | User id of prsnl performing action |
| 11 | `TRACKING_ENCNTR_EXTENSION_ID` | DOUBLE | NOT NULL |  | Primary key |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DC_SIGNED_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PAT_ED_ACKNOWLEDGED_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


# PERSON_ABORH

> Defines the current historical ABO/Rh of a person. Used by transfusion applications to validate the product's ABO/Rh against the patient's ABO/Rh.

**Description:** Person Aborh  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_ABORH_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | The historical ABO group of the person. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time when this row became effective. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LAST_VERIFIED_DT_TM` | DATETIME |  |  | Indicates the date and time that a patient's ABO/Rh was last resulted from a 'HISTRY & UPD' patient ABO/Rh order with the same result as represented by the current row, i.e., patient's ABO/Rh was re-resulted and not changed. |
| 10 | `PERSON_ABORH_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. An internal system-assigned number that makes each row unique. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `RH_CD` | DOUBLE | NOT NULL |  | The historical Rh type of the person (ex. "Pos", "Neg"). |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BB_UPLOAD_PERSON_ABORH_R](BB_UPLOAD_PERSON_ABORH_R.md) | `PERSON_ABORH_ID` |
| [BB_UPLOAD_REVIEW](BB_UPLOAD_REVIEW.md) | `DEMOG_PERSON_ABORH_ID` |
| [BB_UPLOAD_REVIEW](BB_UPLOAD_REVIEW.md) | `UPLOAD_PERSON_ABORH_ID` |
| [PERSON_ABORH_RESULT](PERSON_ABORH_RESULT.md) | `PERSON_ABORH_ID` |


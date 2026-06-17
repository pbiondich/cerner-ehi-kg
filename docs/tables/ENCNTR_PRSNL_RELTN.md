# ENCNTR_PRSNL_RELTN

> The encounter-personnel relationship table contains pointers to related personnel in the personnel table. The kind of relationship (i.e., admitting physician, attending, etc.) defines how the encounter and personnel are related.

**Description:** Encounter Personnel Relationship  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PRSNL_RELTN_ID`  
**Columns:** 35  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_TM` | DATETIME |  |  | This column holds the current system date and time that the row was inserted. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `ENCNTR_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter-person relationship table. It is an internally assigned number and generally not revealed to the user. |
| 13 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Relationship of the prsnl to the encounter |
| 14 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EXPIRATION_IND` | DOUBLE |  |  | Indicates whether the relationship between the encounter and the personnel has expired. |
| 17 | `EXPIRE_DT_TM` | DATETIME |  |  | Date/Time that the relationship has been expired from encounter. Primarily used to prevent the relationship from appearing in PowerChart application. |
| 18 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | Value that shows the type of free text relationship information that is present between the encounter and personnel. When set to a meaning of 'FTBRIEF', this indicates that the prsnl_person_id is NULL, meaning that there is no reference to the personnel table. |
| 19 | `FT_PRSNL_NAME` | VARCHAR(100) |  |  | The name of the personnel in the 'free text' relationship indicated by the free_text_ind in the row being set to 'TRUE'. |
| 20 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | Used within Cerner applications, if necessary, to order encounter personnel relation rows. |
| 21 | `MANUAL_CREATE_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually created the relationship. |
| 22 | `MANUAL_CREATE_DT_TM` | DATETIME |  |  | Date and time the encounter personnel relationship was manually created. |
| 23 | `MANUAL_CREATE_IND` | DOUBLE | NOT NULL |  | Indicates whether the row was manually created. |
| 24 | `MANUAL_INACT_BY_ID` | DOUBLE | NOT NULL |  | The person_id of the person who inactivated the relationship. |
| 25 | `MANUAL_INACT_DT_TM` | DATETIME |  |  | Date and time the row was manually inactivated. |
| 26 | `MANUAL_INACT_IND` | DOUBLE | NOT NULL |  | Indicates whether the row was manually inactivated. |
| 27 | `NOTIFICATION_CD` | DOUBLE | NOT NULL |  | Personnel preferred method of notification for issues concerning related person. |
| 28 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority given to the relation type if more than one of the same type exists |
| 29 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 30 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the row, occurred. This field can be system assigned or manually manipulated by users. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ENCNTR_PRSNL_RELTN_HISTORY](ENCNTR_PRSNL_RELTN_HISTORY.md) | `ENCNTR_PRSNL_RELTN_ID` |
| [TRACKING_ENCNTR_PRSNL_RELTN](TRACKING_ENCNTR_PRSNL_RELTN.md) | `ENCNTR_PRSNL_RELTN_ID` |


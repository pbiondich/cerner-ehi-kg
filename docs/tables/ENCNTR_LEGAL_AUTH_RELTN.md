# ENCNTR_LEGAL_AUTH_RELTN

> The encounter legal authority relationship table contains pointers to legal authority associated with the encounter. Legal authority refers to the approval issued by the court for treating a patient who is committed to the facility for care. For both forensic (committed a crime) and civil (involuntarily hospitalized) patients, the facility requires the legal authority for treatment.

**Description:** Encounter Legal Authority Relationship  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_LEGAL_AUTH_RELTN_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMMITMENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | Identifies the category of the patient's commitment to the facility. |
| 7 | `COMMITMENT_PERIOD` | DOUBLE | NOT NULL |  | The length of time specified in the court order by which the facility has legal authority to hold the patient. |
| 8 | `COMMITMENT_PERIOD_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the unit qualifier (days, hours, etc.) for the commitment period. |
| 9 | `COMMITMENT_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason for the patient's commitment to the facility. |
| 10 | `COMMITMENT_TYPE_FLIP_IND` | DOUBLE | NOT NULL |  | The information indicating if the commitment type for the patient has changed with respect to the previous legal authority for the encounter. |
| 11 | `COUNTY_CD` | DOUBLE | NOT NULL |  | The county code is the code set that value that represents the county which provided the legal authority to treat the patient. |
| 12 | `COURT_ORDER_NUMBER` | VARCHAR(50) |  |  | The identifying number of the court order(s) issued for the patient. |
| 13 | `COURT_ORDER_RECEIVE_DT_TM` | DATETIME |  |  | The date and time at which the facility received the issued court order. |
| 14 | `COURT_ORDER_SIGN_DT_TM` | DATETIME |  |  | The date and time at which the issued court order was signed. |
| 15 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `ENCNTR_LEGAL_AUTH_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the ENCNTR_LEGAL_AUTH_RELTN table. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `LEGAL_AUTHORITY_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the LEGAL_AUTHORITY table that contains various attributes representing the legal authority. |
| 19 | `NEXT_COURT_HEARING_DT_TM` | DATETIME |  |  | The date and time of the patient's next court hearing. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LEGAL_AUTHORITY_ID` | [LEGAL_AUTHORITY](LEGAL_AUTHORITY.md) | `LEGAL_AUTHORITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_LEGAL_AUTH_R_HIST](ENCNTR_LEGAL_AUTH_R_HIST.md) | `ENCNTR_LEGAL_AUTH_RELTN_ID` |


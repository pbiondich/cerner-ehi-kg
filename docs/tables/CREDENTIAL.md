# CREDENTIAL

> This table contains credential records for personnel.

**Description:** Personnel credentials.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREDENTIAL_CD` | DOUBLE | NOT NULL |  | Personnel credential such as MD, RN, CMT, RPh, etc. |
| 7 | `CREDENTIAL_ID` | DOUBLE | NOT NULL |  | The primary key of the Credential table |
| 8 | `CREDENTIAL_TYPE_CD` | DOUBLE | NOT NULL |  | Type of personnel credential such as certification, degree, education, and license. |
| 9 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The display sequence number of the credential in the personnel name full formatted |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `ID_NUMBER` | VARCHAR(50) |  |  | The ID Number of the credential |
| 12 | `NOTIFIED_DT_TM` | DATETIME |  |  | The date when notification was sent to personnel |
| 13 | `NOTIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person id of the notification personnel |
| 14 | `NOTIFY_TYPE_CD` | DOUBLE | NOT NULL |  | Determines the means of communicating with the notification personnel - e.g. e-mail, pager, etc. |
| 15 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id of the address or demographic relationship associated with an address that is used to notify the notification personnel |
| 16 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table from where the parent entity id is used |
| 17 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The prsnl id of the prsnl who has the credential |
| 18 | `RENEWAL_DT_TM` | DATETIME | NOT NULL |  | The renewal date of the credential |
| 19 | `STATE_CD` | DOUBLE | NOT NULL |  | The state/province associated to the credential |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VALID_FOR_CD` | DOUBLE | NOT NULL |  | The amount of time that the credential remains effective. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


# AUTH_DETAIL

> Store detail information related to an authorization/referral

**Description:** AUTHORIZATION DETAIL  
**Table type:** ACTIVITY  
**Primary key:** `AUTH_DETAIL_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZATION_ID` | DOUBLE | NOT NULL | FK→ | Parent (foreign) key to authorization table |
| 6 | `AUTH_COMPANY` | VARCHAR(100) |  |  | Authorizing company |
| 7 | `AUTH_CONTACT` | VARCHAR(100) |  |  | Authorization contact |
| 8 | `AUTH_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique key for the auth_detail record |
| 9 | `AUTH_DT_TM` | DATETIME |  |  | OBSOLETE. The date and time at which insurance company approval was obtained for services being rendered to a patient. This column is deprecated in favor of AUTHORIZATION.AUTH_OBTAINED_DT_TM. |
| 10 | `AUTH_PHONE_NUM` | VARCHAR(100) |  |  | The phone number called to obtain the authorization details |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to long_text table |
| 15 | `PLAN_CONTACT_ID` | DOUBLE | NOT NULL |  | Foreign key to plan_contact record to identify the plan contact used for the auth_detail info |
| 16 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who obtained the detail auth info |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_ID` | [AUTHORIZATION](AUTHORIZATION.md) | `AUTHORIZATION_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AUTH_DETAIL_HIST](AUTH_DETAIL_HIST.md) | `AUTH_DETAIL_ID` |


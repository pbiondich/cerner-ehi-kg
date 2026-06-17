# EEM_DEMOG_DETAIL

> A row represents summary of transaction data

**Description:** Query Demographics Transaction Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIRTH_DT_TM` | DATETIME |  |  | The birth date and time of the person for which the transaction was submitted. If not populated, refer to birth_dt_tm_txt. |
| 2 | `BIRTH_DT_TM_TXT` | VARCHAR(30) |  |  | The birth date and time in ISO date format "YYYY-MM-DDThh:mm:ss.sTZD". |
| 3 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `FIRST_NAME` | VARCHAR(200) |  |  | Patient First Name |
| 5 | `GENDER_CD` | DOUBLE | NOT NULL | FK→ | Patient Gender |
| 6 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Unique Identifier for this table |
| 7 | `LAST_NAME` | VARCHAR(200) |  |  | Patient Last Name |
| 8 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | Key to Organization table |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `PHN` | VARCHAR(200) |  |  | Personal Health Number (Person alias) |
| 11 | `PHN_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The alias pool code of personal health number alias. |
| 12 | `PHN_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | The alias type code used to define the type of alias used a personal health number. |
| 13 | `PROFILE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the profile used for the transaction. A profile contains reference data for outbound messages and is used to define required data to submit the transaction. |
| 14 | `REPLY_DT_TM` | DATETIME |  |  | Reply Date and Time |
| 15 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Transaction sender Identifier |
| 16 | `SENT_DT_TM` | DATETIME | NOT NULL |  | Transaction sent date and time |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GENDER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROFILE_ID` | [EEM_PROFILE](EEM_PROFILE.md) | `PROFILE_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


# REFERRAL_CONTACT

> Records contacts made to the patient for a given referral.

**Description:** Referral Contact  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | FK to the long_text table. A free text field is provided to the user to capture the outcome of the contact. |
| 6 | `CONTACT_DT_TM` | DATETIME |  |  | The date and time the row was created. |
| 7 | `CONTACT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Identifier of the person who made or attempted to make the contact. |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that the row was created. |
| 9 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the phone used for the contact attempt. |
| 10 | `REFERRAL_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row from Referral_Action. |
| 11 | `REFERRAL_CONTACT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a related Referral Contact. |
| 12 | `REFERRAL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related record on the REFERRAL table. |
| 13 | `RESULT_CD` | DOUBLE | NOT NULL |  | The outcome of the contact. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CONTACT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `REFERRAL_ACTION_ID` | [REFERRAL_ACTION](REFERRAL_ACTION.md) | `REFERRAL_ACTION_ID` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |


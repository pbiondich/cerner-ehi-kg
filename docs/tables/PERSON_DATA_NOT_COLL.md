# PERSON_DATA_NOT_COLL

> Stores information describing why person data was not collected.

**Description:** Person Data Not Collected  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BIOMETRIC_IDENT_CD` | DOUBLE | NOT NULL |  | Contains the information describing if the biometric identifier is not collected or why it is not collected for the person |
| 6 | `DRIVERS_LICENSE_CD` | DOUBLE | NOT NULL |  | The information describing if the drivers license is not collected or why it is not collected for the person. |
| 7 | `HOME_ADDRESS_CD` | DOUBLE | NOT NULL |  | Information describing if the home address has not been collected or why the home address has not been collected for the person. |
| 8 | `HOME_EMAIL_CD` | DOUBLE | NOT NULL |  | Information describing if the home email address has not been collected or why the home email address has not been collected for the person |
| 9 | `NATIONAL_HEALTH_NBR_CD` | DOUBLE | NOT NULL |  | The information describing if the national health identification number (NHIN) is not collected or why it is not collected for the person |
| 10 | `PERSON_DATA_NOT_COLL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about why certain person data like SSN, Phone Number, Home Address, etc. has not been collected |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person to whom the information on this record is related. |
| 12 | `PHONE_CD` | DOUBLE | NOT NULL |  | Information describing if the phone number has not been collected or why the phone number has not been collected for the person |
| 13 | `PRIMARY_CARE_PHYSICIAN_CD` | DOUBLE | NOT NULL |  | The information describing if the primary care provider is not collected or why it is not collected for the person |
| 14 | `SSN_CD` | DOUBLE | NOT NULL |  | Information describing if the SSN has not been collected or why the SSN has not been collected for the person |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |


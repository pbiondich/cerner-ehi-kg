# SI_UNMTCHD_PRSN_QUE

> This table stores unmatched person records from inbound messages.

**Description:** System Integration Unmatched Person Queue  
**Table type:** ACTIVITY  
**Primary key:** `SI_UNMTCHD_PRSN_QUE_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | Home address from the inbound message |
| 3 | `ASSIGNING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel assigning person_id to record |
| 4 | `BIRTH_DT_TM` | DATETIME |  |  | Date of birth from message |
| 5 | `BIRTH_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding BIRTH_DT_TM column. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `GENDER_CD` | DOUBLE | NOT NULL |  | Gender code from message |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `MESSAGE_DT_TM` | DATETIME | NOT NULL |  | Date the message entered the system |
| 10 | `NAME_FIRST` | VARCHAR(200) | NOT NULL |  | First name from message |
| 11 | `NAME_LAST` | VARCHAR(200) | NOT NULL |  | Last name from message |
| 12 | `NAME_MIDDLE` | VARCHAR(200) | NOT NULL |  | Middle name from message |
| 13 | `NEW_PERSON_IND` | DOUBLE | NOT NULL |  | Indicates that a new person was created for the unmatched person. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization related to the sending Contributor System |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person related to the Inbound Message |
| 16 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the person match record |
| 17 | `SI_UNMTCHD_PRSN_QUE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 18 | `TELEPHONE_NUMBER` | VARCHAR(50) | NOT NULL |  | Telephone number from message |
| 19 | `UNAUTH_PERSON_ID` | DOUBLE | NOT NULL |  | Person record used to store message information, will be used to combine into the selected person_id |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `ASSIGNING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_UNMTCHD_PRSN_ALIAS](SI_UNMTCHD_PRSN_ALIAS.md) | `SI_UNMTCHD_PRSN_QUE_ID` |


# PERSON_ORG_RELTN

> The person-organization relationship table contains pointers to related organizations in the person table. This table contains data about the type of relationship (I.e., employment, organ donor, student, etc.)

**Description:** Person Organization Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_ORG_RELTN_ID`  
**Columns:** 40  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 9 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 10 | `EMPL_CONTACT` | VARCHAR(100) |  |  | The name of the person at the employer organization to verify employment. |
| 11 | `EMPL_CONTACT_TITLE` | VARCHAR(100) |  |  | The title of the person (empl_contact) at the employer organization who verify employment. |
| 12 | `EMPL_HIRE_DT_TM` | DATETIME |  |  | Date the employee was hired |
| 13 | `EMPL_OCCUPATION_CD` | DOUBLE | NOT NULL |  | The codified representation of the person's type of work performed on behalf of the employer organization. |
| 14 | `EMPL_OCCUPATION_NOMEN_ID` | DOUBLE |  | FK→ | The identifying information of the nomenclature defining the person's type of work performed on behalf of the employer organization. Examples may include Bank Officer, Java Software Developer, and Nurse Practitioner. |
| 15 | `EMPL_OCCUPATION_TEXT` | VARCHAR(100) |  |  | The textual description of the person's type of work performed on behalf of the employer organization. |
| 16 | `EMPL_OCC_INDUSTRY_NOMEN_ID` | DOUBLE |  | FK→ | The identifying information of the nomenclature defining the type of business of the employer organization that compensates the person for work or assigns work to the person as an unpaid worker or volunteer. Examples may include Federal Savings Banks, Computer Software Support Services, and Pharmacies. |
| 17 | `EMPL_POSITION` | VARCHAR(100) |  |  | Employee position is the work position given to the employee by the employer organization. |
| 18 | `EMPL_RETIRE_DT_TM` | DATETIME |  |  | Date the employee retired |
| 19 | `EMPL_STATUS_CD` | DOUBLE | NOT NULL |  | Employee status indicates a condition of employment (I.e., probation, leave, employed, terminated) |
| 20 | `EMPL_TERM_DT_TM` | DATETIME |  |  | Date the employee was terminated |
| 21 | `EMPL_TITLE` | VARCHAR(100) |  |  | Employee title is the work title given to the employee by the employer organization. |
| 22 | `EMPL_TITLE_CD` | DOUBLE | NOT NULL |  | Employee title code is the codified work title given to the employee by the employer organization. |
| 23 | `EMPL_TYPE_CD` | DOUBLE | NOT NULL |  | Employee type identifies the kind of employment related to the number of hours worked and/or how the employee is paid (I.e., part time-hourly, full time-salary, etc.). |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `FREE_TEXT_IND` | DOUBLE |  |  | Indicates whether the relationship is with a free textorganization |
| 26 | `FT_ORG_NAME` | VARCHAR(100) |  |  | The Organization Name entered in free text form. |
| 27 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | Internal Person Management sequence |
| 28 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 29 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 30 | `PERSON_ORG_ALIAS` | VARCHAR(100) |  |  | This is a secondary external identifier for the person organization relationship. |
| 31 | `PERSON_ORG_NBR` | VARCHAR(100) |  |  | This is the primary external identifier for the person organization relationship (I.e., employee number, student id number, etc.) |
| 32 | `PERSON_ORG_RELTN_CD` | DOUBLE | NOT NULL |  | Identifies the specific type of relationship of the person to the organization. This field has Cerner defined meanings (I.e., employee, student, etc.) |
| 33 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person organization relationship table. It is an internal system assigned number. |
| 34 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created |
| 35 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EMPL_OCCUPATION_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `EMPL_OCC_INDUSTRY_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `SPONSOR_PERSON_ORG_RELTN_ID` |
| [PERSON_ORG_RELTN_HIST](PERSON_ORG_RELTN_HIST.md) | `PERSON_ORG_RELTN_ID` |
| [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `SPONSOR_PERSON_ORG_RELTN_ID` |


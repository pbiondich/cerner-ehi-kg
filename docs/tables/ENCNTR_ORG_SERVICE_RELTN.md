# ENCNTR_ORG_SERVICE_RELTN

> Post Acute services provided by an organization for an enounter.

**Description:** Encounter Organization Service Relation  
**Table type:** ACTIVITY  
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
| 5 | `AUTH_NUMBER` | VARCHAR(100) |  |  | The authentication number of the service. |
| 6 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Comments for the organization service relationship. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Encounter table. |
| 8 | `ENCNTR_ORG_SERVICE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the Encntr_org_service_reltn table. |
| 9 | `FINAL_SELECTION_IND` | DOUBLE | NOT NULL |  | Indicator for which organization relationship will be providing the service. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the Organization table. |
| 11 | `PATIENT_REASON_CD` | DOUBLE | NOT NULL |  | The patients reason for selecting the post acute organization to provide the service. |
| 12 | `PAYER_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the payer organization. |
| 13 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority given to the organization relationship per service. |
| 14 | `REFERRING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the referring personnel |
| 15 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | The response from the post acute service organization to the service request. |
| 16 | `RESPONSE_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the response from the post acute service organization to the service request. |
| 17 | `SERVICE_BEG_DT_TM` | DATETIME |  |  | Identifies the date the service should start. |
| 18 | `SERVICE_CD` | DOUBLE | NOT NULL |  | The post acute service to be provided to the encounter by the organization. |
| 19 | `SERVICE_END_DT_TM` | DATETIME |  |  | Identifies the date the service should start. |
| 20 | `SERVICE_FREQUENCY` | VARCHAR(100) |  |  | Frequency of the service to be provided. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PAYER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REFERRING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |


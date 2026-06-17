# PPR_CONSENT_STATUS

> This table contains the consent status for a person at an encounter, org, or person level.

**Description:** PPR Consent Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_ISO` | VARCHAR(8) |  |  | The date for which this table row becomes effective. Normally, this will be the date the row is added, but could be a past or future date in ISO8601 (YYYYMMDD) format |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BLOB_REF_SCAN_ID` | DOUBLE | NOT NULL | FK→ | Blob reference id for a scanned in documents |
| 8 | `COMMENT_TXT` | VARCHAR(250) |  |  | A free text comment for the consent status. |
| 9 | `CONSENT_ID` | DOUBLE | NOT NULL |  | This is the consent_id that is constant across different versions. Use this for the retrieving the data. |
| 10 | `CONSENT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity Id, such as encntr_id, order_catalog_cd etc., |
| 11 | `CONSENT_PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Parent Entity name, such as encounter, order, person etc, |
| 12 | `CONSENT_POLICY_ID` | DOUBLE | NOT NULL | FK→ | The Policy for which the status has been captured. |
| 13 | `CONSENT_STATUS_ID` | DOUBLE | NOT NULL |  | The primary key on this table. |
| 14 | `CONSENT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the Consent. Examples are privacy, record access, consent to treat, etc. |
| 15 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 16 | `DOCUMENT_ON_FILE_IND` | DOUBLE |  |  | Indicator whether the document is on-file. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 20 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | PARENT ENTITY IDENTIFIER |
| 21 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of entity specified in PARENT_ENTITY_ID. |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `REASON_CD` | DOUBLE | NOT NULL |  | The Reason for the status, based on the status. |
| 24 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status of the Consent. |
| 25 | `STATUS_CHANGE_REASON_CD` | DOUBLE | NOT NULL |  | Codified Reason for the change in status. This field will be empty for a new consent |
| 26 | `STATUS_CHANGE_REASON_TEXT` | VARCHAR(255) |  |  | Free Text Reason for the change in status, this will be filled out only if the codified reason has a cdf meaning of OTHER |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_ISO` | VARCHAR(8) |  |  | The date the row was last inserted or updated in ISO8601 (YYYYMMDD) format |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOB_REF_SCAN_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |
| `CONSENT_POLICY_ID` | [PPR_CONSENT_POLICY](PPR_CONSENT_POLICY.md) | `CONSENT_POLICY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |


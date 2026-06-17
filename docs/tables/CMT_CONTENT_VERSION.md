# CMT_CONTENT_VERSION

> Version number for vocabulary. Version information for various 3rd party content (ICD9, ICD10, SNOMED, etc) installed on the client site.

**Description:** community content version  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CMT_CONTENT_VERSION_ID` | DOUBLE | NOT NULL |  | Sequence: Reference_seq This is the value of the unique identifier of the cmt_content_version table. It is an internal system assigned number. |
| 4 | `CONTENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Content version type. 0 - terminology as whole 1 - subset of terminology by vocab_axis 2 - cross mapping |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PACKAGE_NBR` | DOUBLE | NOT NULL |  | Package from which load was run. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 9 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | Code set : 400 The identifier of the vocabulary. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_FT` | VARCHAR(100) |  |  | Free text version number in alphanumeric value. |
| 16 | `VERSION_NUMBER` | DOUBLE |  |  | Version number in numeric value. |
| 17 | `VER_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which the version of the vocabulary becomes effective. |
| 18 | `VER_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time after which the version of the vocabulary is no longer effective. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


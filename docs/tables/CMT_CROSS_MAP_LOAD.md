# CMT_CROSS_MAP_LOAD

> A crossmap links a single SNOMED CT concept to one or more concepts in target terminologies, such as ICD-9-CM, CPT-4, etc. This table is used to upload the latest cross maps and update the CMT_CROSS_MAP table.

**Description:** CMT Cross map Load Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 4 | `CROSS_MAP_FLAG` | DOUBLE |  |  | Cross_map_Flag. Possible values are : 0, = ? |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FORCED_OBS_IND` | DOUBLE |  |  | If the table row is obsolete, but its concept_cki and target_concept_cki are still active on the cmt_concept table, it may be forced into obsoletion. Otherwise, the table row in CMT_CROSS_MAP will not be made obsolete. |
| 7 | `GROUP_SEQUENCE` | DOUBLE | NOT NULL |  | This column used for group sequence |
| 8 | `MAP_TYPE_CD` | DOUBLE | NOT NULL |  | Map Type Code from code set 29223 |
| 9 | `MAP_TYPE_FLAG` | DOUBLE |  |  | Map Type Flag. Possible values are 0 = ?, etc. |
| 10 | `MAP_TYPE_MEAN` | VARCHAR(12) |  |  | The type of cross mapping to indicate whether the SNOMED to ICD-9-cm mapping relationship is one-to-one, or whether the SNOMED concept is more specific or general than the ICD-9-cm code. |
| 11 | `SOURCE_MEAN` | VARCHAR(12) |  |  | The external vocabulary or lexicon that contributed the concept_cki. For example, ICD9, CPT4 etc. |
| 12 | `TARGET_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Contains the target concept_cki to which the concept_cki is mapped. |
| 13 | `TARGET_MEAN` | VARCHAR(12) |  |  | The external vocabulary or lexicon that contributed the target_concept_cki. For example, ICD9, CPT4 etc. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


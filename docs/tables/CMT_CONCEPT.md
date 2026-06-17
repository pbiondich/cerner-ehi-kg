# CMT_CONCEPT

> The cmt_concept table contains one row for each unique meaning or idea. Its purpose is to link alternative names and views of the same concept together and to identify useful relationships between different concepts through the semantic network.

**Description:** The cmt_concept table contains one row for each unique meaning or idea.  
**Table type:** REFERENCE  
**Primary key:** `CONCEPT_CKI`  
**Columns:** 16  
**Referenced by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL | PK | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 7 | `CONCEPT_IDENTIFIER` | VARCHAR(242) | NOT NULL |  | The unique identifier supplied from other external database (e.g. SNOMED) or Cerner and is persistent once it is assigned to a concept. If the concept is from SNOMED, concept identifier is the unique SNOMED Clinical Term identifier provided by CAP. |
| 8 | `CONCEPT_NAME` | VARCHAR(2000) |  |  | A phrase that describes a concept in a way that it is intended to be unambiguous. It is the same as "Fully Specified Name" in SNOMED CT. It explains the meaning of the concept more fully than preferred term. |
| 9 | `CONCEPT_SOURCE_MEAN` | VARCHAR(12) | NOT NULL |  | Represents the source that owns the concept identifier. |
| 10 | `DISALLOWED_IND` | DOUBLE |  |  | An indication of whether the term is allowed for selection or not. 0 - allowed1 - disallowed |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (15)

| From table | Column |
|------------|--------|
| [CMT_CONCEPT_EXPLODE](CMT_CONCEPT_EXPLODE.md) | `CHILD_CONCEPT_CKI` |
| [CMT_CONCEPT_EXPLODE](CMT_CONCEPT_EXPLODE.md) | `PARENT_CONCEPT_CKI` |
| [CMT_CONCEPT_EXTENSION](CMT_CONCEPT_EXTENSION.md) | `CONCEPT_CKI` |
| [CMT_CONCEPT_HISTORY](CMT_CONCEPT_HISTORY.md) | `CONCEPT_CKI` |
| [CMT_CONCEPT_HISTORY](CMT_CONCEPT_HISTORY.md) | `REFERENCE_CONCEPT_CKI` |
| [CMT_CONCEPT_RELTN](CMT_CONCEPT_RELTN.md) | `CONCEPT_CKI1` |
| [CMT_CONCEPT_RELTN](CMT_CONCEPT_RELTN.md) | `CONCEPT_CKI2` |
| [CMT_CONCEPT_RELTN](CMT_CONCEPT_RELTN.md) | `RELATION_CKI` |
| [CMT_CROSS_MAP](CMT_CROSS_MAP.md) | `CONCEPT_CKI` |
| [CMT_SUBSET_MEMBER](CMT_SUBSET_MEMBER.md) | `CHILD_CONCEPT_CKI` |
| [CMT_SUBSET_MEMBER](CMT_SUBSET_MEMBER.md) | `PARENT_CONCEPT_CKI` |
| [CONCEPT_IDENT_BB_CODE](CONCEPT_IDENT_BB_CODE.md) | `CONCEPT_CKI` |
| [CONCEPT_IDENT_BB_DTA](CONCEPT_IDENT_BB_DTA.md) | `CONCEPT_CKI` |
| [CONCEPT_IDENT_MIC_RPT](CONCEPT_IDENT_MIC_RPT.md) | `CONCEPT_CKI` |
| [CONCEPT_IDENT_MIC_SUSC](CONCEPT_IDENT_MIC_SUSC.md) | `CONCEPT_CKI` |


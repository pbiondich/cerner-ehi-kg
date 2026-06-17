# ALLERGY

> The Allergy table contains coded and freetext allergic reaction and adverse effect information about a person

**Description:** Allergy  
**Table type:** ACTIVITY  
**Primary key:** `ALLERGY_INSTANCE_ID`  
**Columns:** 54  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLERGY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely defines an allergy/adverse reaction within the allergy table. The allergy_id can be associated with multiple allergy instances. When a new allergy is added to the allergy table the allergy_id is assigned to the allergy_instance_id. |
| 6 | `ALLERGY_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the allergy table. Each change or revision made to an allergy/adverse reaction creates a new allergy instance. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `CANCEL_DT_TM` | DATETIME |  |  | The date and time that the allergy was set to a status of cancelled. |
| 10 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the person who cancelled the allergy. |
| 11 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason why a reaction has been cancelled. |
| 12 | `CMB_DT_TM` | DATETIME |  |  | Date/Time the item was combined |
| 13 | `CMB_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the combined status of the item. 0 = not part of combined, 1 Combined, 2 Historically Combined, 3 Continuation of Combine indication |
| 14 | `CMB_INSTANCE_ID` | DOUBLE | NOT NULL |  | The "From" person's Allergy instance identifier of the allergy being combined |
| 15 | `CMB_PERSON_ID` | DOUBLE | NOT NULL |  | Person identifier of the "From" person being combined |
| 16 | `CMB_PRSNL_ID` | DOUBLE | NOT NULL |  | Person identifier who performed the combined |
| 17 | `CMB_TZ` | DOUBLE |  |  | Combine Date Time ZoneColumn |
| 18 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 19 | `CREATED_DT_TM` | DATETIME |  |  | The date and time that the allergy/adverse reaction was entered on the allergy profile. |
| 20 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the person who entered the allergy. |
| 21 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 22 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 23 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 24 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 25 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 26 | `ONSET_DT_TM` | DATETIME |  |  | The date that the reaction was identified. |
| 27 | `ONSET_PRECISION_CD` | DOUBLE | NOT NULL |  | indicates to what precision (not entered , age , about , before , after ,unknown) the onset_dt_tm has been set. |
| 28 | `ONSET_PRECISION_FLAG` | DOUBLE |  |  | Indicates to what level of accuracy the onset_dt_tm has been set. 10 = not entered, 20 = Date, 30 = Week Of, 40 = Month, 50 = Year, 60 = Date and Time |
| 29 | `ONSET_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 30 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from ORGANIZATION table primary key |
| 31 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who originally inserted the allergy instanceColumn |
| 32 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 33 | `REACTION_CLASS_CD` | DOUBLE | NOT NULL |  | Identifies the type of reaction, e.g. allergy, adverse drug reaction. |
| 34 | `REACTION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the reaction, e.g. confirmed, cancelled, proposed, working, suspected. |
| 35 | `REACTION_STATUS_DT_TM` | DATETIME |  |  | The date and time the REACTION_STATUS_CD was valued with the current value.Column |
| 36 | `REC_SRC_IDENTIFER` | VARCHAR(50) |  |  | Original source identifier that the allergy was received with from an interface. |
| 37 | `REC_SRC_STRING` | VARCHAR(255) |  |  | Original source string that the allergy was received with from an interface. |
| 38 | `REC_SRC_VOCAB_CD` | DOUBLE | NOT NULL |  | Original source vocabulary that the allergy was received with from an interface. |
| 39 | `REVIEWED_DT_TM` | DATETIME |  |  | Indicated the date and time the allergy was last reviewed by authenticated health care provider. |
| 40 | `REVIEWED_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the authenticated user who has reviewed the allergy. |
| 41 | `REVIEWED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 42 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | Indicates the general severity of the allergy or reaction. |
| 43 | `SOURCE_OF_INFO_CD` | DOUBLE | NOT NULL |  | Identifies the source of the information regarding the reaction, e.g. provider, parent, chart, interface. |
| 44 | `SOURCE_OF_INFO_FT` | VARCHAR(50) |  |  | A free text description of the source of the information. |
| 45 | `SUBSTANCE_FTDESC` | VARCHAR(255) |  |  | A free text description of the substance. |
| 46 | `SUBSTANCE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the substance causing the reaction. |
| 47 | `SUBSTANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of substance, e.g. drug, food, contrast, environment. |
| 48 | `SUB_CONCEPT_CKI` | VARCHAR(255) |  |  | CKI from the concept table which is a functional concept. |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `VERIFIED_STATUS_FLAG` | DOUBLE |  |  | Flag denotes whether the allergy has been verified by pharmacy. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALLERGY_ID` | [ALLERGY](ALLERGY.md) | `ALLERGY_INSTANCE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SUBSTANCE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ALLERGY](ALLERGY.md) | `ALLERGY_ID` |
| [ALLERGY_COMMENT](ALLERGY_COMMENT.md) | `ALLERGY_ID` |
| [ALLERGY_REVIEW_HIST](ALLERGY_REVIEW_HIST.md) | `ALLERGY_INSTANCE_ID` |
| [REACTION](REACTION.md) | `ALLERGY_ID` |


# RESULT

> Stores the current result status for a discrete task assay that is associated with a given patient's order.

**Description:** Result  
**Table type:** ACTIVITY  
**Primary key:** `RESULT_ID`  
**Columns:** 29  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_CONTROL_CELL_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific control cell or the ID of the product of the antibody or antigen test. Blood bank-specific attribute. |
| 2 | `BB_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field stores the unique identifier of the Blood Bank group (rack) used for testing. |
| 3 | `BB_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that is used to group the results for a product or a control cell. Blood bank-specific attribute. |
| 4 | `BIOLOGICAL_CATEGORY_CD` | DOUBLE | NOT NULL |  | Denotes the origin of the sequence of the part of the DNA or RNA being tested and the species of the organism being tested (animal, bacteria, or virus). |
| 5 | `CALL_BACK_IND` | DOUBLE |  |  | Indicates whether a result needs to be called back to the area requesting the procedure to be performed. (Currently not implemented) |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific order catalog procedure associated with a result. |
| 7 | `CHARTABLE_FLAG` | DOUBLE |  |  | Defines if the result should be used for charting/posting to Clinical Events. (Currently not implemented) |
| 8 | `COMMENT_IND` | DOUBLE |  |  | Indicates whether a result comment is associated with the result. A value of 0 means there is not a chartable comment attached to the result. A value of 1 means there is a chartable comment attached to the result. (Currently not implemented) |
| 9 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 10 | `DISPLAY_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Defines the sequence in which the result will be displayed in result entry applications. This attribute is originally derived from the profile_task_r table when the result row is inserted. |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific event ID that relates the result to the clinical event tables. (Currently not implemented) |
| 12 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field stores the unique identifier of the reagent lot used for testing. |
| 13 | `NC_COMMENT_IND` | DOUBLE |  |  | Indicates whether a result footnote is associated with the result. A value of 0 indicates there are no non-chartable footnotes for the result. A value of 1 indicates there are non-chartable footnotes for the result. (Currently not implemented) |
| 14 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific order. Creates a relationship to the orders table. |
| 15 | `PENDING_IND` | DOUBLE | NOT NULL |  | Indicates whether this result must be performed before the order it is associated with should be considered complete. This attribute is originally derived from the profile_task_r table when the result row is written. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | The result chosen as most accurate among all results for a given assay concept. Determines what displays in the person level viewer for inherited results. |
| 18 | `REPEAT_NUMBER` | DOUBLE |  |  | Defines the number of times the procedure has been repeated to produce a result. (Currently not implemented) |
| 19 | `RESTRICT_DISPLAY_IND` | DOUBLE | NOT NULL |  | Restricts the display of the result in result entry to only those that have results associated with them. This attribute is originally derived from the profile_task_r table when the result row is written. |
| 20 | `RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific result. |
| 21 | `RESULT_PROCESSING_CD` | DOUBLE | NOT NULL |  | A unique code value used to determine result processing. For Helix result entry applications, this field determines the column in which the result appears. |
| 22 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the current status of the result, such as performed, verified, corrected, and so on. |
| 23 | `SECURITY_LEVEL_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific security level for the result. (Currently not implemented) |
| 24 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific discrete task assay associated with the result. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |
| `LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [ABO_TESTING](ABO_TESTING.md) | `RESULT_ID` |
| [BB_EXCEPTION](BB_EXCEPTION.md) | `RESULT_ID` |
| [INSTRUMENT_IMAGE](INSTRUMENT_IMAGE.md) | `RESULT_ID` |
| [PERFORM_RESULT](PERFORM_RESULT.md) | `RESULT_ID` |
| [PERSON_ABORH_RESULT](PERSON_ABORH_RESULT.md) | `RESULT_ID` |
| [PERSON_ANTIBODY](PERSON_ANTIBODY.md) | `RESULT_ID` |
| [PERSON_ANTIGEN](PERSON_ANTIGEN.md) | `RESULT_ID` |
| [PERSON_RH_PHENOTYPE](PERSON_RH_PHENOTYPE.md) | `RESULT_ID` |
| [PERSON_RH_PHENO_RESULT](PERSON_RH_PHENO_RESULT.md) | `RESULT_ID` |
| [RESULT_COMMENT](RESULT_COMMENT.md) | `RESULT_ID` |
| [SPECIAL_TESTING_RESULT](SPECIAL_TESTING_RESULT.md) | `RESULT_ID` |
| [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `RESULT_ID` |


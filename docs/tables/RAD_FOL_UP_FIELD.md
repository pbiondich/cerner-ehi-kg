# RAD_FOL_UP_FIELD

> The Rad_Fol_Up_Field table contains fields used for classification of a performed exam.

**Description:** Rad Follow Up Field  
**Table type:** REFERENCE  
**Primary key:** `FOLLOW_UP_FIELD_ID`  
**Columns:** 24  
**Referenced by:** 26 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_CODED_FIELD` | VARCHAR(10) |  |  | The BI-RADS code that corresponds with this field. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BIRAD_GROUP_TXT` | VARCHAR(25) |  |  | Used to define which birad group the nmd_group_code_nbr applies to. |
| 4 | `CERNER_MEANING_STR` | VARCHAR(25) |  |  | This column contains a unique string that can be used by Cerner applications. |
| 5 | `EDITION_NBR` | DOUBLE |  |  | This column indicates what ACR edition the follow up field is a part of. Edition 2 and edition 3 do not have decimal precision and will be assumed to mean 2.0 and 3.0. Starting with edition 3.1, the edition number appearing in the column on the table will be assumed to have a single decimal precision. In other words, edition 3.1 will be appear as 31 on the table. |
| 6 | `FIELD_DESCRIPTION` | VARCHAR(255) |  |  | The Field_Description is a textual description for a follow up field. |
| 7 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | The Field_Type_Flag indicates if if the follow up field is a numeric entry or a coded value. |
| 8 | `FOLLOW_UP_FIELD_ID` | DOUBLE | NOT NULL | PK | The Follow_Up_Field_Id uniquely identifies a row in the Rad_Fol_Up_Field table. It serves no otherpurpose other than to uniquely identify the row. |
| 9 | `HISTFORM_PRINT_IND` | DOUBLE | NOT NULL |  | A table row may be printed on the mammography patient history form. A value of 1 indicates that this row will be printed whereas any other value will cause the row not to print on the history form. |
| 10 | `MODALITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of modality group. |
| 11 | `MODIFY_FLAG` | DOUBLE |  |  | The Modify_Flag indicates if the follow up field is a standard field vs. a user defined field.It also indicates if a field is required and if it is modifiable or not. |
| 12 | `MORE_COMPLETE_AUDIT_IND` | DOUBLE | NOT NULL |  | Indicates if this field participates in the More Complete audit report generation. 0 = does not participate, 1 = does participate |
| 13 | `NMD_GROUP_CODE_TXT` | VARCHAR(5) | NOT NULL |  | Identifies the standard NMD code for this field. |
| 14 | `PARENT_ID` | DOUBLE | NOT NULL | FK→ | This column is used to facilitate the hierarchy among the fields. It is a foreign key to the Rad_Fol_Up_Field table. |
| 15 | `RANGE_MAX` | DOUBLE |  |  | The Range_Max field contains the maximum value of a range that is specified for a numeric response. |
| 16 | `RANGE_MIN` | DOUBLE |  |  | The Range_Min field contains the minimum value of a range that is specified for a numeric response. |
| 17 | `REFERENCE_CD` | DOUBLE | NOT NULL |  | The Reference_Cd field provides a way to assign follow up fields to groups according to where they appear in the conversation. |
| 18 | `SEQUENCE` | DOUBLE |  |  | The sequence identifies the order in which the field is to be displayed in mammography case maintenance. |
| 19 | `SPECIAL_PROCESS_FLAG` | DOUBLE |  |  | Special processing flag used by case maintenance |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |

## Referenced by (26)

| From table | Column |
|------------|--------|
| [MAMMO_ASSESSMENT_SERIES](MAMMO_ASSESSMENT_SERIES.md) | `ASSESSMENT_ID` |
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `BREAST_COMP_ID` |
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `CHANGES_ID` |
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `PRIOR_SURG_FOL_UP_ID` |
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `SIDE_ID` |
| [MAMMO_FIND](MAMMO_FIND.md) | `LESION_CLASS_ID` |
| [MAMMO_FIND](MAMMO_FIND.md) | `PATH_ID` |
| [MAMMO_FIND_DETAIL](MAMMO_FIND_DETAIL.md) | `FIELD_ID` |
| [MAMMO_LETTER](MAMMO_LETTER.md) | `RECOMMENDATION_ID` |
| [MAMMO_PROBLEM](MAMMO_PROBLEM.md) | `PROBLEM_ID` |
| [MAMMO_RECOMMEND_SEQ](MAMMO_RECOMMEND_SEQ.md) | `RECOMMENDATION_ID` |
| [MAMMO_RECOMMEND_SERIES](MAMMO_RECOMMEND_SERIES.md) | `RECOMMENDATION_ID` |
| [MAMMO_RISK](MAMMO_RISK.md) | `FACTOR_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `ASSESSMENT_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `REASON_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `RECOMMENDATION_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `STAT_CAT_ID` |
| [MAMMO_USER_DEF](MAMMO_USER_DEF.md) | `FIELD_ID` |
| [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `PARENT_ID` |
| [RAD_MAMMO_LETTER_MGMT_R](RAD_MAMMO_LETTER_MGMT_R.md) | `FOLLOW_UP_FIELD_ID` |
| [RAD_MAMMO_STUDY_ASSESS_MGMT_R](RAD_MAMMO_STUDY_ASSESS_MGMT_R.md) | `FOLLOW_UP_FIELD_ID` |
| [RAD_OMF_MAMMO_DETAILS](RAD_OMF_MAMMO_DETAILS.md) | `FOLLOW_UP_FIELD_ID` |
| [RAD_OMF_MAMMO_FIND_DETAILS](RAD_OMF_MAMMO_FIND_DETAILS.md) | `FOLLOW_UP_FIELD_ID` |
| [RAD_PROCEDURE_ASSOC](RAD_PROCEDURE_ASSOC.md) | `INDICATION_FOR_EXAM_ID` |
| [RAD_TEMPLATE_GROUP](RAD_TEMPLATE_GROUP.md) | `ASSESSMENT_ID` |
| [RAD_TEMPLATE_GROUP](RAD_TEMPLATE_GROUP.md) | `RECOMMENDATION_ID` |


# SHX_ELEMENT

> Each row on the table represents Social History category view.

**Description:** SHX_ELEMENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIDENTIAL_IND` | DOUBLE |  |  | A flag to indicate if confidentiality enabled(1) or disabled (0) |
| 2 | `ELEMENT_SEQ` | DOUBLE | NOT NULL |  | Identifies the ordering of this element relative to other elements contained within a section. |
| 3 | `INPUT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Code set 4002169. Unique code value that identifies the default control type for the element. |
| 4 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if a response is required for the element. 1=True, 0=False |
| 5 | `RESPONSE_LABEL` | VARCHAR(255) | NOT NULL |  | Label that appears in the overall assessment of the category for a given element |
| 6 | `RESPONSE_LABEL_LAYOUT_FLAG` | DOUBLE | NOT NULL |  | Layout of the element label. It can be 0 - Before, 1 - After or 2 - Instead Result. |
| 7 | `SHX_CATEGORY_DEF_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from the PROBLEM_SECTION_DEF table The unique identifier for a Social History category view. It will be used to uniquely identify a category. |
| 8 | `SHX_ELEMENT_ID` | DOUBLE | NOT NULL |  | This is the table's primary key. The unique identifier for a Social History category view. It will be used to uniquely identify a category and an element. |
| 9 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Code set 14003. Unique code value that identifies a specific discrete task assay. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INPUT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SHX_CATEGORY_DEF_ID` | [SHX_CATEGORY_DEF](SHX_CATEGORY_DEF.md) | `SHX_CATEGORY_DEF_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |


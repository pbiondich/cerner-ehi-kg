# ONC_TASK_SENT_RELTN

> Stores the oncology task assay and anatomy pathology sentence association information

**Description:** ONC TASK SENTENCE RELATION  
**Table type:** REFERENCE  
**Primary key:** `ONC_TASK_SENT_RELTN_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOC_SET_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Primary key from DOC_SET_ELEMENT_REF table, in this case used identify the documentation set element. |
| 3 | `DOC_SET_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from DOC_SET_ELEMENT_REF, in this case used to identify the specific version of a documentation set section. |
| 4 | `ONC_TASK_SENT_RELTN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `ONC_WORKSHEET_ID` | DOUBLE | NOT NULL | FK→ | Primary key from ONC_WORKSHEET table,in this case used get the doc set and worksheet association information from ONC_WORKSHEET |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Defines information that further defines this element. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_ELEMENT_ID` | [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_ELEMENT_ID` |
| `DOC_SET_SECTION_ID` | [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `DOC_SET_SECTION_REF_ID` |
| `ONC_WORKSHEET_ID` | [ONC_WORKSHEET](ONC_WORKSHEET.md) | `ONC_WORKSHEET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ONC_NOMEN_TERM_RELTN](ONC_NOMEN_TERM_RELTN.md) | `ONC_TASK_SENT_RELTN_ID` |


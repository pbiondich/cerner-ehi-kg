# MIC_ORGANISM_DATA

> This table contains reference information relating to organisms defined on code set 1021.

**Description:** Microbiology Organism Data  
**Table type:** REFERENCE  
**Primary key:** `ORGANISM_ID`  
**Columns:** 12  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANISM_ID` | DOUBLE | NOT NULL | PK | This field identifies the code value of the organism from code set 1021. |
| 2 | `ORGANISM_TYPE` | DOUBLE |  |  | This field indicates the type of organism associated with this record. Valid values include: 1 = Bacteria 2 = Mycobacteria 3 = Fungus 4 = Parasite 5 = Virus 6 = Yeast |
| 3 | `ORG_CLASS_FLAG` | DOUBLE |  |  | This field identifies the classification of the organism associated with this record. Organisms are associated with a classification at the time they are defined in the Organism tool. |
| 4 | `PARENT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the parent organism associated with this record. For example, if this is an organism record its parent organism would be the genus to which it is associated.The hierarchical levels associated with organisms is organisms are associated with genuses. Genuses are associated with families. Families are associated with sections. All hierarchical relationshi |
| 5 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether the organism if used in a report task should set the culture to positive. Valid values include: 0 = Negative 1 = Positive |
| 6 | `QC_IND` | DOUBLE |  |  | This field is not used at this time. |
| 7 | `REPORT_NAME` | CHAR(15) |  |  | This field is not used at this time. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `ORGANISM_CD` |
| [MIC_EVENT_LOG](MIC_EVENT_LOG.md) | `ORGANISM_CD` |
| [MIC_ORGANISM_ID](MIC_ORGANISM_ID.md) | `ID_ORGANISM_CD` |
| [MIC_PATHOGEN](MIC_PATHOGEN.md) | `PATHOGEN_CD` |
| [MIC_REQUIRED_TASK](MIC_REQUIRED_TASK.md) | `ORGANISM_CD` |
| [MIC_SUS_FIRST_LEVEL_INTERP](MIC_SUS_FIRST_LEVEL_INTERP.md) | `ORGANISM_GROUPING_CD` |
| [MIC_TASK_LOG](MIC_TASK_LOG.md) | `ORGANISM_CD` |
| [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `ORGANISM_GROUPING_CD` |
| [MIC_VALID_SUS_RESULT](MIC_VALID_SUS_RESULT.md) | `ORGANISM_CD` |


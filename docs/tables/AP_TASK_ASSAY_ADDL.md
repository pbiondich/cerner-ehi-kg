# AP_TASK_ASSAY_ADDL

> This reference table contains parameters defined for pathology processing tasks that relate to inventory (specimen, cassette, and/or slide) and identification code associations (the identification codes to prompt for when the task is ordered).

**Description:** AP Task Assay Additional Info  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTOVERIFY_WORKFLOW_CD` | DOUBLE | NOT NULL |  | Contains the value representing the workflow step for auto verification should be. |
| 2 | `CREATE_INVENTORY_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether or not the completion of the associated processing task (discrete task) causes one or more pathology inventory records to be created. |
| 3 | `DATE_OF_SERVICE_CD` | DOUBLE | NOT NULL |  | This column defines the date of service value(case collection date, current date, case received date, charge task order date) for ap billing tasks. |
| 4 | `HALF_SLIDE_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not slides created from the associated processing task (discrete task) are considered half slide or full slide for the purposes of calculating cytology screening slide counts. |
| 5 | `PRINT_LABEL_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the associated processing task (discrete task) should cause a slide label to print if the task qualifies for selection parameters entered by the user in the label print application. |
| 6 | `PRINT_WORKLIST_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the associated processing task (discrete task) should cause an entry to be included on a worklist if the task qualifies for selection parameters entered by the user in the worklist application. |
| 7 | `SLIDE_ORIGIN_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether a task that creates slide inventory represents a slide created directly from a specimen, or a slide created from a block. |
| 8 | `STAIN_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the processing task is associated with the creation of a stained slide (or the staining of a previously-created slide). |
| 9 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the processing task (discrete task) for which inventory and identification associations have been established on the AP_TASK_ASSAY_ADDL reference table. |
| 10 | `TASK_ASSAY_TYPE_CD` | DOUBLE |  |  | Defines the Category Type of the Processing Task. Ex: Special Stain, IHC Stain. |
| 11 | `TASK_TYPE_FLAG` | DOUBLE |  |  | This field contains a numeric flag value documenting the most specific level of inventory association that is associated with the processing task identified in the TASK_ASSAY_CD field. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |


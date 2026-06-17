# AP_PROCESSING_GRP_R

> This reference table contains the processing group tasks created for pathology. Group processing tasks are not created using the Order Catalog and Departmental Order Catalog. Instead, these groupings are defined using this table.

**Description:** AP Processing Group Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_LEVEL` | DOUBLE |  |  | This field contains a beginning sequence value that will be used to assign the slide identification code for the associated processing task (discrete task). |
| 2 | `BEGIN_SECTION` | DOUBLE |  |  | This field contains a beginning sequence value that will be used to assign the block/cassette identification code for the associated processing task (discrete task). |
| 3 | `END_LEVEL` | DOUBLE |  |  | This field contains an ending sequence value that will be used to assign the slide identification code for the associated processing task (discrete task). |
| 4 | `END_SECTION` | DOUBLE |  |  | This field contains the ending sequence value that will be used to assign the block/cassette identification code for the associated processing task (discrete task). |
| 5 | `GROUPER_CD` | DOUBLE | NOT NULL |  | This column is obsolete. |
| 6 | `MULTIPLIER` | DOUBLE |  |  | This field is not used at this time. |
| 7 | `NO_CHARGE_IND` | DOUBLE |  |  | This field contains an indicator designating whether or not the task included within the processing group should be defaulted as no charge in the task order entry application. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the 'processing group reltn' row is related (CODE_VALUE from the CODE_VALUE table, PROTOCOL_ID from the AP_SPECIMEN_PROTOCOL table). |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this 'processing group reltn' row is related (CODE_VALUE or AP_SPECIMEN_PROTOCOL). |
| 10 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a sequence value that, when combined with the PARENT_ENTITY_NAME and PARENT_ENTITY_ID fields, make the unique table key value. |
| 11 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the processing task (discrete task) associated with the processing group task. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |


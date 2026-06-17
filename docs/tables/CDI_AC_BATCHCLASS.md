# CDI_AC_BATCHCLASS

> This table defines CPDI configurations for Ascent Capture Batch Classes.

**Description:** CPDI Ascent Capture Batch Classes.  
**Table type:** REFERENCE  
**Primary key:** `CDI_AC_BATCHCLASS_ID`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_CONTRIB_SRC_CD` | DOUBLE | NOT NULL |  | Specifies the contributor source to use when resolving document type aliases for this batch class. |
| 3 | `AUDITING_IND` | DOUBLE | NOT NULL |  | Specifies whether or not to include this batch class for auditing and reporting. |
| 4 | `AUTO_CLOSE` | DOUBLE | NOT NULL |  | Specifies if the batch should be closed automatically when auto process is completed successfully. |
| 5 | `AUTO_COMP_NOTIFY` | DOUBLE | NOT NULL |  | Specifies if the validation operated should be notified when the batch has finished auto processing. |
| 6 | `BATCHCLASS_NAME` | VARCHAR(32) | NOT NULL |  | Ascent capture batch class name. |
| 7 | `BATCH_PROFILE_IND` | DOUBLE | NOT NULL |  | indicates that this is a batch profile (batch class) for use in KTA Advanced Capture |
| 8 | `CDI_AC_BATCHCLASS_ID` | DOUBLE | NOT NULL | PK | Unique ID for the batch class. |
| 9 | `CPDI_BATCH_CLASS_IND` | DOUBLE | NOT NULL |  | Indicates if this is a CPDI batch class (1) or a Kofax batch class (0). |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The ID of the organization the batch class is associated to. |
| 11 | `SINGLE_ENCNTR` | DOUBLE | NOT NULL |  | Specifies if the batch class is meant for single encounter batches. User will be prompted if the batch contains documents for multiple encounters. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CDI_AC_BATCHCLASS_PARENT_R](CDI_AC_BATCHCLASS_PARENT_R.md) | `CDI_AC_BATCHCLASS_ID` |
| [CDI_DOCUMENT_TYPE](CDI_DOCUMENT_TYPE.md) | `CDI_AC_BATCHCLASS_ID` |
| [CDI_PENDING_BATCH](CDI_PENDING_BATCH.md) | `CDI_AC_BATCHCLASS_ID` |


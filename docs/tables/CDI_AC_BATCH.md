# CDI_AC_BATCH

> This table is used to track statistics for batches created in Kofax Capture. This data is copied from the third party system to this table by the CPDI Audit Service.

**Description:** CDI Ascent Capture Batch  
**Table type:** ACTIVITY  
**Primary key:** `CDI_AC_BATCH_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCHCLASS` | VARCHAR(32) | NOT NULL |  | Name of the Kofax batch class on which the batch is based. |
| 2 | `BATCHCLASSDESCRIPTION` | VARCHAR(80) | NOT NULL |  | Description of the Kofax batch class on which the batch is based. |
| 3 | `BATCHNAME` | VARCHAR(128) | NOT NULL |  | Name assigned to the batch when it is created. |
| 4 | `CDI_AC_BATCH_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is internally generated. |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time when the batch was created. |
| 6 | `CREATIONSTATIONID` | VARCHAR(32) | NOT NULL |  | Identifies the Kofax Capture station where the batch was created. The Station ID is assigned during the Kofax installation process. |
| 7 | `CREATIONUSERID` | VARCHAR(50) | NOT NULL |  | If the User Profiles feature is enabled, this is the Kofax Capture login ID for the user who created the batch. If the feature is not enabled, this is the Windows login name for the user who created the batch. If a Windows login name is not required, the value is listed as "Unknown". |
| 8 | `CREATIONUSERNAME` | VARCHAR(80) | NOT NULL |  | If the User Profiles feature is enabled, this is the user name assigned in the profile of the user who created the batch. If the feature is not enabled, this is the Windows login name for the user who created the batch. If a Windows login name is not required, the value is listed as "Unknown". |
| 9 | `EXTERNAL_BATCH_IDENT` | DOUBLE | NOT NULL |  | Unique incremental value assigned to each batch that is created at a Kofax Capture site. |
| 10 | `TRANSFERID` | VARCHAR(38) | NOT NULL |  | Reserved for use by Kofax Capture. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDI_AC_BATCHMODULE](CDI_AC_BATCHMODULE.md) | `CDI_AC_BATCH_ID` |
| [CDI_BATCH_SUMMARY](CDI_BATCH_SUMMARY.md) | `CDI_AC_BATCH_ID` |


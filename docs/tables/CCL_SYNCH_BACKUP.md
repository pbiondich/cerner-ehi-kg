# CCL_SYNCH_BACKUP

> Stores backup CCL dictionary objects for use in merging objects during upgrades and RDDS processing

**Description:** CCL Synchronize Backup  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CCLGROUP` | DOUBLE | NOT NULL |  | Discern Explorer Group |
| 2 | `CCL_SYNCH_BACKUP_ID` | DOUBLE | NOT NULL |  | Primary Key - Unique row identifier |
| 3 | `CHECKSUM` | DOUBLE | NOT NULL |  | calculated checksum value |
| 4 | `DIC_DATA0` | VARCHAR(810) | NOT NULL |  | Discern Explorer data record, stored in little-endian format (VMS, Linux, Windows) |
| 5 | `DIC_DATA1` | VARCHAR(810) | NOT NULL |  | Discern Explorer data, stored in big-endian format (AIX, HP-UX) |
| 6 | `DIC_KEY0` | VARCHAR(40) | NOT NULL |  | Discern Explorer data key referencing DPROTECT or DCOMPILE key, stored in little-endian format (VMS, Linux, Windows) |
| 7 | `DIC_KEY1` | VARCHAR(40) | NOT NULL |  | Discern Explorer data key referencing DPROTECT or DCOMPILE key, stored in big-endian format (AIX, HP-UX) |
| 8 | `DIR_NAME` | VARCHAR(20) | NOT NULL |  | The directory name the object was included from in the source domain |
| 9 | `ENDIAN_PLATFORM` | DOUBLE | NOT NULL |  | The endian type of the source export platform |
| 10 | `MAJOR_VERSION` | DOUBLE | NOT NULL |  | Discern Explorer major version |
| 11 | `MINOR_VERSION` | DOUBLE | NOT NULL |  | Discern Explorer minor version |
| 12 | `NODE_NAME` | VARCHAR(20) | NOT NULL |  | UNIX/VMS node name |
| 13 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Discern Explorer Object Name |
| 14 | `OBJECT_TYPE` | VARCHAR(1) | NOT NULL |  | Discern Explorer Object Type |
| 15 | `QUAL` | DOUBLE | NOT NULL |  | Discern Explorer sequence value to maintain order of DCOMPILE rows |
| 16 | `RCODE` | VARCHAR(1) | NOT NULL |  | Discern Explorer rcode (DPROTECT rows= 5, DCOMPILE rows= 9) |
| 17 | `TIMESTAMP_DT_TM` | DATETIME | NOT NULL |  | The date/time stamp which indicates when the object was last modified in the source export domain. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


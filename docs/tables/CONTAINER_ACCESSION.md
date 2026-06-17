# CONTAINER_ACCESSION

> The resolution table between containers and accessions. This table will tell you what containers belong to an accession.

**Description:** Container Accession  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | A string that uniquely identifies a specimen. |
| 2 | `ACCESSION_CONTAINER_NBR` | DOUBLE |  |  | A number uniquely identifying a particular container on an accession. |
| 3 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies an accession number. |
| 4 | `BARCODE_ACCESSION` | VARCHAR(20) |  |  | The string printed on a label to uniquely identify the specimen. This string is the accession number truncated. |
| 5 | `CONTAINER_ALIAS_CD` | DOUBLE | NOT NULL |  | An alias for the sontainer suffix. |
| 6 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies a container. |
| 7 | `OVERRIDE_CONT_ID_PRINT_FLAG` | DOUBLE | NOT NULL |  | An override value for the container ID print setting normally applied from the collection class. 0 - Use default collection class setting; 1 - Print the Container ID in the barcode and on the label; 2 - Do not print the container ID in the barcode or on the label. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


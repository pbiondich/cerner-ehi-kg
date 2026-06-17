# MIC_VALID_ORGANISM

> This table associates the service_resource/procedure/source combination to the valid_organism_id on the mic_valid_organism_mbr table.

**Description:** Valid Organisms  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the service resource. Service resource code values are stored on code set 221. |
| 3 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the source. Source code values are stored on code set 2052, 1150, 1151. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALID_ORGANISM_ID` | DOUBLE | NOT NULL |  | Id that represents a unique service resource, procedure, and source combination for valid organisms. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


# MIC_VALID_CODED_RESPONSE

> Associates the service_resource/procedure/source combination to a valid_response_id on the mic_valid_response_mbr table

**Description:** Valid coded responses  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the service resource . Service resource code values are stored on code set 221. |
| 3 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the code value assigned to the source. Source code values are stored on code sets 2052, 1150,1151. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALID_RESPONSE_ID` | DOUBLE | NOT NULL |  | This is represents a unique combination of service_resource, procedure, and source for valid responses |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._


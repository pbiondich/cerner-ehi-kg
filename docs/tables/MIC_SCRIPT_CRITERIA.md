# MIC_SCRIPT_CRITERIA

> This reference table contains the criteria that an associated script is assigned to.

**Description:** Microbiology Script Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the 'body site' to which the MIC_SCRIPT is assigned. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the orderable procedure to which the MIC_SCRIPT is assigned. This could be used to join to the ORDER_CATALOG table. |
| 3 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the 'organism' to which the MIC_SCRIPT is assigned. |
| 4 | `ORGANISM_QUANTITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the 'organism quantity' to which the MIC_SCRIPT is assigned. |
| 5 | `PATIENT_LOCATION_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the patient location to which the MIC_SCRIPT is assigned. This could be used to join to the LOCATION table. |
| 6 | `SCRIPT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the parent MIC_SCRIPT table. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the service resource to which the MIC_SCRIPT is assigned. This could be used to join to the SERVICE_RESOURCE table. |
| 8 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the 'source' to which the MIC_SCRIPT is assigned. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRIPT_ID` | [MIC_SCRIPT](MIC_SCRIPT.md) | `SCRIPT_ID` |


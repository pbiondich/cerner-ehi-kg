# RESOURCE_ACCESSION_R

> Creates a relationship between the service resource and the accessions available for resulting quality control at that instrument or bench.

**Description:** Resource Accession Resolution  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific quality control accession number. Creates a relationship to the accession table. |
| 2 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific control material associated with the service resource and quality control accession. Creates a relationship to the control material table. |
| 3 | `FREQ_MIN` | DOUBLE |  |  | Determines how often the control should be run for the instrument or bench to which it is assigned. |
| 4 | `INSTR_XREF` | VARCHAR(20) |  |  | Used to post QC results from an instrument. Identifies a cross reference for the accession number for instruments. This field is used by instruments for posting QC results and must be filled out for posting QC results to work. |
| 5 | `PREACTIVE_IND` | DOUBLE |  |  | Indicates whether the quality control accession is pre-active. A value of 0 denotes the accession as not pre-active. A value of 1 denotes the accession as pre-active. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies a specific service resource associated with a quality control accession. |
| 7 | `SYMBOLOGY` | VARCHAR(2) |  |  | Defines which bar code symbology for which this service resource/QC accession is set up. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |


# MIC_INSTR_TRANS

> This table contains the translation information for all codes transmitted from a susceptibility instrument interface to the Cerner system. This includes organisms, antibiotics, panels, sources, susceptibility results, susceptibility methods, and automate

**Description:** Microbiology Instrument Translation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MICRO_ALIAS` | VARCHAR(20) | NOT NULL |  | This field identifies the description of the code as it exists on the host system(instrument) and identifies how the code will be transmitted to and from the Cerner system. |
| 2 | `MICRO_CD` | DOUBLE | NOT NULL |  | The microbiology code is the code set value of the row. This includes translations for source, procedure, medication, panel, |
| 3 | `MICRO_FLAG` | DOUBLE | NOT NULL |  | This field identifies the type of translation. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument for which translations are defined. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |


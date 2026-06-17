# CNT_EQUATION

> CONTENT EQUATION INFORMATION

**Description:** CNT EQUATION  
**Table type:** REFERENCE  
**Primary key:** `CNT_EQUATION_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_FROM_MINUTES` | DOUBLE | NOT NULL |  | defines the beginning age range defined for the calculation. |
| 3 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | Code Set: 66 a unique code value that identifies the units of age for the beginning of the age range. |
| 4 | `AGE_FROM_UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Age From Units Code Value |
| 5 | `AGE_TO_MINUTES` | DOUBLE | NOT NULL |  | defines the ending age range defined for the calculation. |
| 6 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | Code Set: 66 a unique code value that identifies the units of age for the ending of the age range. |
| 7 | `AGE_TO_UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Age To Units Code Value |
| 8 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) FK from CNT_DTA_KEY2 |
| 9 | `CNT_EQUATION_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID - PRIMARY KEY |
| 10 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | indicates whether the equation is the default equation for the procedure. |
| 11 | `EQUATION_DESCRIPTON` | VARCHAR(2000) |  |  | character description for the equation that is parsed when the equation is performed by the resulting application. |
| 12 | `EQUATION_ID` | DOUBLE | NOT NULL |  | a unique, internal, system-assigned number that identifies a specific equation. |
| 13 | `EQUATION_POSTFIX` | VARCHAR(2000) |  |  | stores the equation in a postfix format. used mainly for instrument processing. |
| 14 | `EQUATION_UID` | VARCHAR(100) | NOT NULL |  | UNIQUE IDENTIFIER FOR THE EQUATION |
| 15 | `GESTATIONAL_AGE_IND` | DOUBLE | NOT NULL |  | indicates whether the equation applies to gestational age. a value of 0 indicates the equation is not for gestational age. a value of 1 indicates the equation is for gestational ages. |
| 16 | `SCRIPT_NAME` | VARCHAR(50) |  |  | defines a site-specific script to be used for interpretations. (currently not implemented) |
| 17 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Code Set: 221 a unique code value that identifies the service resource associated with the equation. a value of zero means all service resources. |
| 18 | `SERVICE_RESOURCE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Service Resource Code Value |
| 19 | `SEX_CD` | DOUBLE | NOT NULL |  | Code Set: 57 a unique code value that identifies the sex of the person for which the equation is to be used. |
| 20 | `SEX_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Sex Code Value |
| 21 | `SPECIES_CD` | DOUBLE | NOT NULL |  | Species code from Code Set: 226 |
| 22 | `SPECIES_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Species Code Value |
| 23 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | a unique code value that identifies a specific discrete task assay. |
| 24 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 25 | `UNKNOWN_AGE_IND` | DOUBLE | NOT NULL |  | indicates whether the equation is for patients with an unknown age or birth date. a value of 0 indicates the equation is not used for patients with unknown ages or birth dates. a value of 1 indicates the equation is for patients with unknown ages or birth dates. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CNT_EQUATION_COMPONENT](CNT_EQUATION_COMPONENT.md) | `CNT_EQUATION_ID` |


# MIC_REF_ANG

> This table takes the combination of service resource/procedure/source and creates a unique identifier that is used to define the report and disqualification parameters for automatic no growth reporting.

**Description:** The criteria table for Auto No Growth  
**Table type:** REFERENCE  
**Primary key:** `ANG_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each procedure/service resource/source combination. Thisidentifier is then used to uniquely identify the parameters on tables such as mic_ang_ref_report and mic_ang_disqual tables. |
| 2 | `AUTOMATED_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the procedure/service resource/source combination will have automated auto no growth reporting performed for this combination. If this field is not set to Yes thenthis combination will not be included in automatic no growth report processing. Valid values include: 0 = Not include in automatic no growth report processing 1 = Included in automatic no growth re |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 4 | `PRESUMPTIVE_POSITIVE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the System allows for stopping the automatic no growth process for the culture when a presumptive positive message is received from an interfaced instrument. valid values include: 1 = System allows Stopping ANG |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the instrument or bench for which automatic no growth times are defined. |
| 6 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define auto no growth reporting parameters. All three levels of source hierarchy (source, section, category) can be used in defining auto nogrowth reporting parameters. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_ANG_DISQUAL](MIC_ANG_DISQUAL.md) | `ANG_ID` |
| [MIC_ANG_STATUS](MIC_ANG_STATUS.md) | `ANG_ID` |
| [MIC_REF_ANG_REPORT](MIC_REF_ANG_REPORT.md) | `ANG_ID` |


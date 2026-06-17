# BB_MOD_POOL_NBR

> Stores the pooled product number sequence buckets associated with a given pooling modification option. These sequence buckets are used to by the system to automatically generate unique product numbers when pooling products.

**Description:** Blood Bank Modification Pooled Product Number  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ISBT_SUPPLIER_FIN` | VARCHAR(5) |  |  | The Facility Identification supplier which is in the product number barcode. (Alphanumeric) |
| 2 | `MOD_POOL_NBR_ID` | DOUBLE | NOT NULL |  | The internal system assigned number that uniquely identifies a blood bank pooled product number sequence bucket. |
| 3 | `OPTION_ID` | DOUBLE | NOT NULL | FK→ | The internal system assigned number that uniquely identifies a modification option. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Obsolete. This column is no longer used. Uniquely identifies the organization that is creatin the pool. It will display as supplier on the label. |
| 5 | `PREFIX` | VARCHAR(10) | NOT NULL |  | Pooled product number prefix for system generated product numbers. |
| 6 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Pooled product number sequence number for system generated product numbers. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `YEAR` | DOUBLE | NOT NULL |  | Pooled product number year for system generated product numbers. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPTION_ID` | [BB_MOD_OPTION](BB_MOD_OPTION.md) | `OPTION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |


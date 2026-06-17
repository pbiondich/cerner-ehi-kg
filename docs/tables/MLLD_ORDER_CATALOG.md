# MLLD_ORDER_CATALOG

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_ORDER_CATALOG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Indicates date orderable was approved by Multum |
| 3 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | This field contains Multum's identification codes for generic drugs. These are extremely important codes for developers who are using Multum's database products because they serve as the primary link to all of Multum's advanced clinical services. Multum's drug_id is always of the form "d#####". |
| 4 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL |  | This field contains a (unique ?) numeric identifier for a description of a drug. This value comes from an outside source and is not generated in Millennium. |
| 5 | `HIDE_IND` | DOUBLE |  |  | Indicates whether the orderable should be viewable during ordering. |
| 6 | `MNEMONIC_TYPE` | VARCHAR(40) | NOT NULL |  | Defines the default type of synonym for the order catalog |
| 7 | `ORDER_ENTRY_FORMAT` | VARCHAR(50) |  |  | Default order entry format for orderable. |
| 8 | `OVERRIDE_MNEMONIC_TYPE` | VARCHAR(40) |  |  | Indicates mnemonic_type to be used if different for dose range checking |
| 9 | `RX_MASK` | DOUBLE |  |  | Default rx_mask for orderable. |
| 10 | `SKIP_IND` | DOUBLE | NOT NULL |  | indicates whether synonym should be ignored with future updates. 0 - do not skip (default); 1 - skip |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

